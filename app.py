from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'yatsu_rally_2026_secret_key'

# 5つのスタンプの設定
STAMPS = {
    "hori": {"name": "八つ堀のしみず谷津", "img": "八ッ堀.png", "is_hotaru": True},
    "tenjin": {"name": "天神谷津", "img": "天神谷津.png", "is_hotaru": True},
    "oshidori": {"name": "おしどりの里", "img": "おしどり.png", "is_hotaru": True},
    "hi": {"name": "谷津の日 (82)", "img": "谷津の日.png", "is_hotaru": False},
    "walk": {"name": "谷津ウォーク 2026", "img": "谷津ウォーク.png", "is_hotaru": False}
}

@app.route('/')
def index():
    if 'my_stamps' not in session:
        session['my_stamps'] = []
    
    just_got = request.args.get('just_got')
    just_got_name = STAMPS[just_got]['name'] if just_got in STAMPS else None
    my_stamps = session['my_stamps']
    
    has_hotaru = any(s in my_stamps for s in ["hori", "tenjin", "oshidori"])
    has_hi = "hi" in my_stamps
    has_walk = "walk" in my_stamps

    clear_normal = has_hotaru and has_hi
    clear_special = has_hotaru and has_hi and has_walk

    # ➔ ここで「stamps=STAMPS」としてHTMLにデータを送っています！
    return render_template('index.html', 
                           stamps=STAMPS, 
                           my_stamps=my_stamps, 
                           just_got_name=just_got_name,
                           clear_normal=clear_normal,
                           clear_special=clear_special)

@app.route('/stamp/<stamp_id>')
def get_stamp(stamp_id):
    if 'my_stamps' not in session:
        session['my_stamps'] = []
        
    if stamp_id in STAMPS:
        my_stamps = session['my_stamps']
        if stamp_id not in my_stamps:
            my_stamps.append(stamp_id)
            session['my_stamps'] = my_stamps
            session.modified = True
            return redirect(url_for('index', just_got=stamp_id))
            
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session['my_stamps'] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)