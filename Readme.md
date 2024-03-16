Readme File

Django rest framework project using default database sqlite

```
#run migrations
python manage.py migrate
# run djnago server
python manage.py runserver
```

In this project, we have 3 different apps Customer, Plan, Subscriber.
Customer is an user who can Subscribe one telecom Plan.

RelationShip
Two standalone entities: Customer and Plan

Customer is a foreignkey to Subscriber Model.
Plan is a foreignkey to Subscriber Model.

# API
Three API endpoints 
- to create subscriber POST /subscribers/
- to list all subscribers GET /subscribers/
- to update the subscription plan of a subscriber PUT /subscribers/{subscriber_id}/