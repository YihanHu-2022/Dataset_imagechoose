from unittest import result
from flask import Flask, jsonify, render_template, request
from flask import make_response, json
import os


import func

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        name = request.form.get('search')
        fid = request.form.get('idtext')
        fit = request.form.get('fit')
        ordinary = request.form.get('ordinary')
        unfit = request.form.get('unfit')
        previous = request.form.get('previous')
        next_img = request.form.get('next_img')
        if name:
            ImgList = func.get_img_file(name)
            img = func.imagelist_to_attr(ImgList)
            data = {
                'name': img[0].name,
                'id': img[0].id,
                'index': img[0].index,
                'score': img[0].score,
                'src': img[0].src
            }
            print(data)
            data_json = json.dumps(data, ensure_ascii=False)
            return render_template('main.html', data=data_json)

        elif fid:
            src_now = request.form['idsearchbtn']
            print(src_now)
            name_split = src_now.split('/')[-2]
            name = name_split.split('/')[-1]
            result = func.id_search(name, fid)
            img = result
            data = {
                'name': result.name,
                'id': result.id,
                'index': result.index,
                'score': result.score,
                'src': result.src
            }
            print(data)
            data_json = json.dumps(data, ensure_ascii=False)
            return render_template('main.html', data=data_json)
        elif fit:
            src_now = request.form['fit']
            src_now = src_now.split('static/')[1]
            with open('score.txt', 'a') as output:
                output.write(src_now + "\nfit\n")
            name_split = src_now.split('/')[-2]
            name = name_split.split('/')[-1]
            id_split = src_now.split('/')[-1]
            src_in = os.path.join(name, id_split)
            result = func.get_next_image(src_in)
            if result == False:
                return render_template('error.html')
            else:
                img = result
                data = {
                    'name': result.name,
                    'id': result.id,
                    'index': result.index,
                    'score': result.score,
                    'src': result.src
                }
                print(data)
                data_json = json.dumps(data, ensure_ascii=False)
                return render_template('main.html', data=data_json)
        elif ordinary:
            src_now = request.form['ordinary']
            src_now = src_now.split('static/')[1]
            print(src_now)
            with open('score.txt', 'a') as output:
                output.write(src_now+"\nordinary\n")
            name_split = src_now.split('/')[-2]
            name = name_split.split('/')[-1]
            id_split = src_now.split('/')[-1]
            src_in = os.path.join(name, id_split)
            result = func.get_next_image(src_in)
            if result == False:
                return render_template('error.html')
            else:
                img = result
                data = {
                    'name': result.name,
                    'id': result.id,
                    'index': result.index,
                    'score': result.score,
                    'src': result.src
                }
                print(data)
                data_json = json.dumps(data, ensure_ascii=False)
                return render_template('main.html', data=data_json)
        elif unfit:
            src_now = request.form['unfit']
            src_now = src_now.split('static/')[1]
            print(src_now)
            with open('score.txt', 'a') as output:
                output.write(src_now+"\nunfit\n")
            name_split = src_now.split('/')[-2]
            name = name_split.split('/')[-1]
            id_split = src_now.split('/')[-1]
            src_in = os.path.join(name, id_split)
            result = func.get_next_image(src_in)
            if result == False:
                return render_template('error.html')
            else:
                img = result
                data = {
                    'name': result.name,
                    'id': result.id,
                    'index': result.index,
                    'score': result.score,
                    'src': result.src
                }
                print(data)
                data_json = json.dumps(data, ensure_ascii=False)
                return render_template('main.html', data=data_json)
        elif previous:
            src_now = request.form['previous']
            name_split = src_now.split('/')[-2]
            name = name_split.split('/')[-1]
            id_split = src_now.split('/')[-1]
            src_in = os.path.join(name, id_split)
            result = func.get_pre_image(src_in)
            if result == False:
                return render_template('error.html')
            else:
                img = result
                data = {
                    'name': result.name,
                    'id': result.id,
                    'index': result.index,
                    'score': result.score,
                    'src': result.src
                }
                print(data)
                data_json = json.dumps(data, ensure_ascii=False)
                return render_template('main.html', data=data_json)
        elif next_img:
            src_now = request.form['next_img']
            name_split = src_now.split('/')[-2]
            name = name_split.split('/')[-1]
            id_split = src_now.split('/')[-1]
            src_in = os.path.join(name, id_split)
            result = func.get_next_image(src_in)
            if result == False:
                return render_template('error.html')
            else:
                img = result
                data = {
                    'name': result.name,
                    'id': result.id,
                    'index': result.index,
                    'score': result.score,
                    'src': result.src
                }
                print(data)
                data_json = json.dumps(data, ensure_ascii=False)
                return render_template('main.html', data=data_json)


if __name__ == '__main__':
    app.run()