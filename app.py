from flask import Flask, render_template

app = Flask(__name__)

SERVICES = [{
  "id":
  1,
  "title":
  "Design",
  "description":
  "We listen carefully to our clients' business needs, and design customized solutions that fit their requirements and budget. We create proposals that outline the key milestones, timeline, and pricing to help our clients make informed decisions."
}, {
  "id":
  2,
  "title":
  "Implement",
  "description":
  "We take project management seriously. We will closely monitor the progress of your project and ensure it stays on track, meeting all established milestones. After implementation, we will conduct comprehensive testing to ensure the solution is functioning optimally before it goes live."
}, {
  "id":
  3,
  "title":
  "Maintain",
  "description":
  "We provide ongoing support, maintenance, and assistance for any future changes or questions our clients may have. Our solutions are built to be highly secure and reliable, ensuring long-term success for our clients."
}]


@app.route("/")
def hello_world():
  return render_template('home.html', services=SERVICES)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
