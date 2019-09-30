# 0x14. Javascript - Web scraping

## Learning Objectives
* Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
* How to manipulate JSON data
* How to use request and fetch API
* How to read and write a file using fs module

## Resources
* [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
* [request module](https://github.com/request/request)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/node
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
* All your files must be executable
* The length of your files will be tested using wc
* You are not allowed to use var

### Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```

### Install `request` module and use it
[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

---

## TASKS

### [0. Readme](./0-readme.js)
* Write a script that reads and prints the content of a file.


### [1. Write me](./1-writeme.js)
* Write a script that writes a string to a file.


### [2. Status code](./2-statuscode.js)
* Write a script that display the status code of a GET request.


### [3. Star wars movie title](./3-starwars_title.js)
* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.


### [4. Star wars Wedge Antilles](./4-starwars_count.js)
* Write a script that prints the number of movies where the character “Wedge Antilles” is present.


### [5. Loripsum](./5-request_store.js)
* Write a script that gets the contents of a webpage and stores it in a file.


### [6. How many completed?](./6-completed_tasks.js)
* Write a script that computes the number of tasks completed by user id.


### [7. Who was playing in this movie?](./100-starwars_characters.js)
* Write a script that prints all characters of a Star Wars movie:


### [8. Right order](./101-starwars_characters.js)
* Write a script that prints all characters of a Star Wars movie:


### [9. Twitter Auth](./102-search_twitter.js)
* Write a Javascript script that takes in 3 strings and sends a search request to the Twitter API

---

## Author
* **Nga La** - [sungnga](https://github.com/sungnga)