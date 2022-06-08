# mozio_task

#### Coverage Record: 99%

### DEPLOYMENT ON HEROKU

##### URL
    https://mozio-task.herokuapp.com/

### 1.Polygon Endpoints

##### 1.1 GET: LIST
    https://mozio-task.herokuapp.com/<lat>/<long>

### 2.Provider Endpoints

##### 2.1 POST
    https://mozio-task.herokuapp.com/provider/
Data: {name, phone_number, email, language, currency}

##### 2.2.1 GET: LIST
    https://mozio-task.herokuapp.com/provider/

##### 2.2.2 GET: RETRIEVE
    https://mozio-task.herokuapp.com/provider/<str:pk>

##### 2.3 PUT
    https://mozio-task.herokuapp.com/provider/<str:pk>
    
##### 2.4 DELETE
    https://mozio-task.herokuapp.com/provider/<str:pk>


### 3.Service Area Endpoints

##### 3.1 POST
    https://mozio-task.herokuapp.com/service-area/
Data: {name, price, long, lat, provider}

##### 3.2.1 GET: LIST
    https://mozio-task.herokuapp.com/service-area/

##### 3.2.2 GET: RETRIEVE
    https://mozio-task.herokuapp.com/service-area/<str:pk>

##### 3.3 PUT
    https://mozio-task.herokuapp.com/service-area/<str:pk>
    
##### 3.4 DELETE
    https://mozio-task.herokuapp.com/service-area/<str:pk>
