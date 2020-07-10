from flask import Flask, render_template, request, jsonify
from Logic.MarkovChains import Chains

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET", "POST"])
def home():
    return render_template("home_page.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/_background_process", methods = ["GET", "POST"])
def background_process():
    try:
        # Get information from the html with the button press
        order = float(request.args.get("order"))
        chains = Chains(order = int(order), 
                        filename = "Data/poems Baijron_clean.txt",
                        length = 50)
        output = chains.getPoem(rest = False)
        return jsonify(result = output)
    except:
        pass
    
@app.route("/api/v1/poem", methods=["GET"])
def api_all():
    try:
        if "order" in request.args:
            order = int(request.args["order"])
        else:
            return "Ошибка: Степень последовательности не указана. Пожалуйста укажите 'order' в api запросе. "       
        chains = Chains(order = order, 
                        filename = "Data/poems Baijron_clean.txt",
                        length = 50)
        output = chains.getPoem(rest = True)
        return jsonify(result = output)
    except:
        pass
        

if __name__ == "__main__":
    app.run(debug = False)
