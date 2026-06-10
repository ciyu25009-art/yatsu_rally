from flask import Flask, render_template

app = Flask(__name__)

CHECKPOINTS = ["yatsu-01", "yatsu-02", "yatsu-03", "yatsu-04"]

@app.route('/')
def index():
    return render_template('index.html', checkpoints=CHECKPOINTS)

@app.route('/stamp/<point_id>')
def get_stamp(point_id):
    if point_id in CHECKPOINTS:
        return render_template('get_stamp.html', point_id=point_id)
    return "無効なスタンプポイントです", 404

if __name__ == '__main__':
    app.run(debug=True)