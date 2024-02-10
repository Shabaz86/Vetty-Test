from flask import Flask, request, render_template, abort
import chardet

app = Flask(__name__)


@app.route('/readfile/', defaults={'filename': 'file1.txt'})
@app.route('/readfile/<filename>')
def readfile(filename):
    start_line = request.args.get('start_line', default=1, type=int)
    end_line = request.args.get('end_line', default=None, type=int)

    try:
        with open(filename, 'rb') as f:
            result = chardet.detect(f.read())

        with open(filename, 'r', encoding=result['encoding']) as file:
            lines = file.readlines()
            content = ''.join(lines[start_line-1:end_line])
    except FileNotFoundError:
        abort(404, description="File not found")
    except Exception as e:
        abort(500, description=str(e))

    return render_template('index.html', content=content)


@app.errorhandler(404)
def resource_not_found(e):
    return render_template('error.html', message=e), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', message=e), 500


if __name__ == "__main__":
    app.run(debug=True)
