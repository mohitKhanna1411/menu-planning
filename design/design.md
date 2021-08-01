# Tech Stack

- Python 3
- Flask as web framework
- PeeWee as ORM
- Docker as Container
- SQLite as a database
- Pytest for unit test
- Postman for API test
- Swagger UI for API Documentation
# System Achitecture

![System Architecture Diagram](System-arch-menu-planning.png?raw=true "System Architecture")
## Presentation Layer
- The scope of the project was not to implement the frontend.
- Instead of creating a frontend, Swagger UI documentation for REST API is created.
- This allows to communicate with the application layer via HTTP requests and responses.
- This provides a quick API working check and is a well documented UI which gives information about the API.

## Application Layer
- This layer contains all the bussiness logic of the application.
- The menu-planning microservice is containerzied using Docker.
- This microservice can now be used as a plug-n-play service for any existing product.
- The enpoints are developed using Python and Flask.
- - /auth - POST apis for login and signup, gives JWT token in return. This token is sent in subsiquent requests for user authentication.
- - /recipe - POST api to create a new recipe and its steps and ingredients. GET api to fetch the recipe by uuid. PUT is to update the existing recipe by uuid. DELETE to delete a recipe by uuid. GET list api to list all the exisiting recipes in the database
- - /menu - POST api to create a new menu and its contained recipes. GET api to fetch the menu by uuid. PUT is to update the existing menu by uuid. DELETE to delete a menu by uuid. GET list api to list all the exisiting menus in the database
- - /review - POST api to create a new review for menu or recipe. GET api to fetch the review by uuid. PUT is to update the existing review by uuid. DELETE to delete a review by uuid. GET list api to list all the exisiting reviews in the database
- All the corresponding functions are written using python and its libraries
- These functions create corresponding entity classes whihc are later mapped to the database in the data layer.

## Data Layer
- This layer is developed using SQLite relational databse.
- The recommended stack had postgres but SQLite does similar work using SQL. Though it is not scable and less powerful than postgres but does the work in this project.
- Objects gets passed to the Object Relation Mapping (ORM) from the application layer
- This ORM is developed using python peewee.
- Peewee maps the entity to the SQLite database and using CRUD operations does the talking with the db.
- Data storage uses SQLite.(Can easily be replaced by postgres anytime)


# ER Diagram

![ER Diagram](ER-menu-planning.png?raw=true "ER Diagram")

## Explaination of the above daigram

- Recipe table has columns such as `id as primary key`, uuid, classification, other meta etc.
- Recipe has many steps. Hence, there is a `1:N realtion` between Recipe and Steps table.
- Steps table has columns like image_line, description etc and `recipe_id as a foriegn key` from Recipe table.
- Recipe has many ingredients. Hence, there is a `1:N relation` between Recipe and Ingredients table.
- Ingredients table has columns like image_line, name etc and `recipe_id as a foriegn key` from Recipe table.
- Menu table has columns such as `id as primary key`, uuid, week, year, other meta etc.
- Many menus can have many recipes. Hence there is a `M:N relation` between Menu and Recipe Table.
- Whenever we have M:N realtion we create another table and here we create another table with `recipe_id as foreign key` from Recipe Table and `menu_id as foreign key` from Menu table.
- Review table has columns such as `id as primary key`, uuid, comments, ratings, other meta etc.
- One recipe can have many reviews. Hence we have `1:N relation` and `recipe_id as foreign key` in Review table.
- One menu can have many reviews. Hence we have `1:N relation` and `menu_id as foreign key` in Review table.