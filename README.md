## What is it?

It is a repository that contains several scripts to fetch japanese celebrities' name, avatar and introduction from Internet and to generate a Anki deck finally.

## How to get the Anki deck?

You can go to the [release page](https://github.com/masakichi/japanese_celebrity/releases) to get the `japanese_celebrity.apkg` directly without running scripts in this repository.

## Run scripts yourself

### step 1: initial environment

```
git clone https://github.com/masakichi/japanese_celebrity.git
cd japanese_celebrity
pipenv install
pipenv shell
```

### step 2: run scrapy 

Run `scrapy crawl pasonica -o celebrity.json`, after it finished, you will get a JSON file called `celebrity.json`


### step 3: clean data

Run `python clean_data.py`, after it finished, you will get a JSON file called `celebrity_clean.json`(will be used for downloading images), and a CSV called `celebrity.csv`(will be imported to Anki)

### step 4: download images

1. build go file `download_images.go` by running `go build download_images.go`, binnary file `download_images` will be generated.

2. make `images` folder by running `mkdir images`.

3. run `./download_images` then you will get all avatars in images folder.
