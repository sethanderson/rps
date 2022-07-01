from flask import Flask, render_template, request
from app_helper import get_waifu_pic, for_work_text, get_categories


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", req_path=request.path)


@app.route("/waifu/")
def my_waifus():
    return render_template("waifu.html", req_path=request.path)


@app.route("/waifu/<for_work>/")
def get_categories_list(for_work):
    return render_template(
        "categories.html",
        req_path=request.path,
        title=f"{for_work_text(for_work)} Categories",
        categories=get_categories(for_work),
    )


@app.route(f"/waifu/<for_work>/<category>/")
def get_waifu(for_work, category):
    return render_template(
        "waifu_pic.html",
        req_path=request.path,
        title=f"Here is your {category} {for_work_text(for_work)} waifu",
        waifu_pic=get_waifu_pic(for_work, category),
    )


if __name__ == "__main__":
    app.run(debug=True)
