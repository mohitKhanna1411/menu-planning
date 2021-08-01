# Menu Planning Service


## Steps
```
cd menu-planning
docker-compose build
docker-compose up
```

## API Documentation

```
http://localhost:8090/static/swagger-ui/index.html
```

## System Design

Please read [DESIGN](design/design.md) file added in the repo

## E2E Test

- Make sure you have you npm installed in your local machine
```
npm -v

npm i newman

cd menu-planning/main-app/main-app/tests/E2E-Tests

newman run MenuPlanningService.postman_collection.json
```

- Alternatively, import MenuPlanningService.postman_collection.json file into your postman app and run the collection.

## Unit Test

