from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hello, World!</h1>
        <p><a href="/form">Pergi ke Halaman Form</a></p>
    '''

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'''
            <h2>Data Diterima</h2>
            <p>Nama: {name}</p>
            <p>Email: {email}</p>
            <a href="/">Kembali ke Halaman Utama</a>
        '''
    return '''
        <form method="POST">
            Nama: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            <input type="submit" value="Kirim">
        </form>
        <br>
        <a href="/">Kembali ke Halaman Utama</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
