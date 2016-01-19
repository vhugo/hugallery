# Hugallery [![Build Status: Linux](https://travis-ci.org/vhugo/hugallery.svg?branch=master)](https://travis-ci.org/vhugo/hugallery)

> A command line script to generate static photo albums with [PhotoSwipe](http://photoswipe.com/) for [Hugo](http://gohugo.io/) sites.

## Table of Contents

* [Getting Started](#getting-started)
	* [Install](#install)
	* [Usage](#usage)
	* [Setting up the album and photos](#setting-up-the-album-and-photos)
		* [album.json](#albumjson)
		* [photos.csv](#photoscsv)
	* [After set up](#after-set-up)
	* [Hugo themes and album layouts](#hugo-themes-and-album-layouts)
* [License](#license)


## Getting started

Make sure you have a folder for your album with all photos you want
to post inside it. If you want to see the results from this tool, check out
[my site](//vhugo.github.io/gallery/). Here is a screenshots.

![alt My album gallery][vhugo_gallery]

### Install

In order for *Hugallery* to work with photos, you will need to install
[ImageMagick](http://www.imagemagick.org/script/binary-releases.php).
Then just run the following command to easily install.

```
pip install git+https://github.com/vhugo/hugallery.git
```

### Usage


First time you run the command for a new album folder, it will create the
configuration files you need, if you already have it configured, then it should generate the
photo album inside Hugo project, if you don't know
[how to configure](#setting-up-the-album-and-photos), check the next section.

```
hugallery /my-album-folder/
```

### Setting up the album and photos

*Hugallery* uses a couple of configuration files to create the album,
those files are `album.json` and `photos.csv`.

#### album.json

Your `album.json` should look something like this:

```json
{
    "album_name": "Your Album Name",
    "hugo_location": "/your/hugo/site/directory/",
    "max_size": 900,
    "max_thumbnail_size": 164
}
```

Make sure **hugo_location** has the location of your Hugo site project.

#### photos.csv

You can use any spreadsheet editor that supports CSV files to edit
`photos.csv`, when you first open it should look something like this:

| cover | order | title | description | filename    |
|:----- |:-----:|:-----:|:-----------:| -----------:|
|  True |     0 |       |             | photo01.jpg |
|       |     1 |       |             | photo02.jpg |
|       |     2 |       |             | photo03.jpg |
|       |   ... |       |             |     ...     |
|       |    20 |       |             | photo20.jpg |

- `cover`: just type "True" if you want the photo as cover of your album
- `order`: position the photos is going to be displayed
- `title`: title for the photo (when the file is created this is shown as empty)
- `description`: also known as photo caption (when the file is created this is shown as empty)
- `filename`: this information is used by the script so please **do not change it**

#### After set up

Once you have update the configuration files, just run the script as
shown on *[usage](#usage)* section.

### Hugo themes and album layouts

*Hugallery*  will add two files, `gallery/single.html` and
`section/gallery.html`, in Hugo project's `layouts` folder. Change those
files to adapt the gallery to your current theme. When changing these
files, make sure you include the PhotoSwipe JS and CSS files in the theme's
header and/or footer.


## License

Licensed under the MIT License. See the
[LICENSE](https://github.com/vhugo/hugallery/blob/master/LICENSE) file
for more details.

[vhugo_gallery]: http://i.imgur.com/cLycJfD.png