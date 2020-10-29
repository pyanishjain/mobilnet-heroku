check flask app wtih heroku
hsoted : https://trashflask.herokuapp.com/

here i am using keras mobilnet how to host deep learning model in hroku ,
as heroku has limit of 500Mb

please check requirement.txt file to get dependenies
it takes about 420MB / 500MB of disk space

i try with fastai but takes about 890MB of diskspace hence it is not possibel to host fastai model with heroku



Run Locally
to run locally 
1) pip install -r requirements.txt
2) add in main.py
    if "__name__" == "__main__":
            app.run()
3) python main.py

## host on heroku
see docs
1) dowload heroku cli
2) login hroku

## just searvch flask heroku and you got amazings blogs
