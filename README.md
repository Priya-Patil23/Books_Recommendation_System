<h1>Book Recommendation System</h1>
<h2>This project is made with two approaches: Popularity based recommnedation and Collaborative filtering based recommendation.</h2>
<p>The dataset is been taken from the kaggle platform</p>
<a href="https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset">Here's the link for the dataset</a>
<p>There are three files in the dataset: book , users and ratings. First goal is to 
    take up the 10 most popular books and show them on the home page. The condition
    for choosing the books is that we will take those books only which are rated by at least
    250 people. Then we are storing those popular books in one dataframe with the data
    of their authors, images and ratings.
</p>
<p>Second goal is to build collaborative filtering based recommendation. Here we are actually assuming that
    each book is a single point in "number of users rated" dimensions. Again we have applied
    certain conditions like we will choose those books only which are rated by more than 200
    people and the most important we will choose users only who have rated more than 
    50 books. We are creating the pivot table for the same and then finding the distance of
    each book with others and saving it in the dataframe. Now this dataframe is useful 
    for recommendation which will check the closest point to it and collect the data about that point.
</p>
<p>The First page that is home page will show the top 10 books and there will be an option 
    of recommend. When one will click that button then the user will be directed to other page
    where he or she have to enter the full name of the book and accordingly the recommendation will
    be generated and shown.
</p>
