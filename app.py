from flask import Flask , render_template , request
import numpy as np
import pickle

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pivot.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similar.pkl','rb'))

pt.index = [x.lower().strip() for x in pt.index]
books["Book-Title"] = [x.lower().strip() for x in books["Book-Title"]]
# We can also remove the punctuations but let it be for now.


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' ,
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           rating=list(popular_df['avg rating'].values)
                           )

@app.route('/home')
def index1():
    return render_template('index.html' ,
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           rating=list(popular_df['avg rating'].values))

@app.route('/recommend')
def recommned():
    return render_template("index2.html")


@app.route('/predict' , methods = ["post"])
def predict():
    input = request.form.get('bookname')
    try:
        index = np.where(pt.index == str(input).lower().strip())[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)

        return render_template('index2.html', data=data)
    except:
        return render_template('index3.html',
                               book_name=list(popular_df['Book-Title'].values),
                               author=list(popular_df['Book-Author'].values),
                               image=list(popular_df['Image-URL-M'].values),
                               rating=list(popular_df['avg rating'].values))



if __name__ == '__main__':
    app.run( port = 5000 , host = "0.0.0.0")


