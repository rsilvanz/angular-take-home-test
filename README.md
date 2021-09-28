## Facteon's Django Take Home Test

### Pre-test Instructions

```
1.) install the project requirements `pip install -r ./requirements.txt`
2.) run the server `python3 manage.py runserver`
3.) Navigate to  `localhost:8000/`
4.) Happy coding!
```

### Challenge Instructions
```
This challenge was designed to take no longer than 2 hours to complete. 
Please do not spend any longer than 4 hours in total in solving the following tasks. 
Please read each question in its entirety before attempting a solution.
Unit Tests are encouraged but not compulsory.
Sample data to be used in the challenge can be found in db.sqlite3. 
Feel free to Add or Extend the database, but do not delete the data with your submission.
Make sure to add any new pip package dependencies to the requirements.txt file.
```

```
django_take_home is based around a new django new service being built which provides api users access to assets which we call `EquipmentLocation`s. 

Example: `Auckland Site` > `chair manufacturing line 1` > `group 1` > `molding rig` > `quality sensor station`. 

Equipment locations are references to 'assets of equipment which exist at locations'. 
Equipment Locations exist in a tree relationship, where that tree can have an arbitrary number of levels. 
Equipment locations also have categories. 
The 3 main categories of Equipment location are `site`, `line` and `machine`. 
In the example above, `Auckland Site` would be a site,  `chair manufacturing line 1` would be a line, and everything else is considered to be a machine.
 ```

_1.) A system user wants to see a breadcrumb path of each equipment node. A system user wants to know how many machines exist as a subset under a given location._

    Write functions that generate computed properties for `EquipmentLocation`.

    i) `EquipmentLocation`.`location_path` which is a forward-slash-separated slugified path for each equipment. An example of the format necessary for `Some Line` would be: `some_site / some_line`
        
    ii) `EquipmentLocation`.`number_of_machines` which is the total number of machines under this node (the number of children this node has).
    
    iii) Implement a solution which reduces the query time taken to the database for these properties.
     
Requirements:
* Let the `parent_id` of the model be used to implement the tree relationship between nodes. 
* The `location_path` must be a forward-slash-separated, slugified path to the node in the tree. eg. "some_site / some_line / some_equipment"
* The `location_path` must be automatically generated based on the `name` field of the `EquipmentLocation` node, and all its ancestors in the branches of its tree. If `name` changes for any branch from anywhere in the system, have some mechanism so that `location_path` changes also.
* The `number_of_machines` must be automatically generated based on number of nodes which are directly and indirectly descendant of the current `EquipmentLocation` node. If a change to the system increases or decreases the number of children for an `EquipmentLocation`, then this property must also reflect it.

2.) _An api user wants to create and read the references to their equipment from the system. An api user wants to be able to obtain their equipment in a tree-like structure._

    Using DRF and REST best-practises, implement CREATE and READ in CRUD for data within the `EquipmentLocation` model as API endpoints. 
    You are responsible for implementing the API design you feel fit however, the data contract must match the field names and structure in the sample payload.  
    
Requirements:
* Atleast 2 Endpoints should be accessible under `/location/` url structure.
* Let the parent_id of the model be used to implement the tree relationship between nodes.
* The `order` field of the model must be respected in the payload generated (order the nodes by lowest first).
* The api endpoints must show up at localhost:8000/ within the swagger app.
* The READ implementation should produce a payload similar to the sample below.

Sample Serialized Payload for the object:
```json
{
  "id": 1,
  "type_id": 1,
  "name": "Some Site",
  "site_id": 1,
  "line_id": null,
  "location_path": "some_site",
  "part_number": null,
  "manual_id": null,
  "children": [{
      "id": 2,
      "type_id": 2,
      "name": "Some Line",
      "site_id": 1,
      "line_id": 2,
      "location_path": "some_site / some_line",
      "part_number": null,
      "manual_id": null,
      "children": [{
          "id": 3,
          "type_id": 3,
          "name": "Some Machine",
          "site_id": 1,
          "line_id": 2,
          "location_path": "some_site / some_line / some_machine",
          "part_number": "QWERTY123",
          "manual_id": 1,
          "children": null      
      }]  
  }] 
}

```

3.) _An api user wants to upload multiple documents which relate to a single machine. Increase the limit of one document, to 5 documents per equipment_. 


    `EquipmentLocation`s currently have single manuals. 
    These are related documents such as pdfs or xls files stored by a separate service. 
    As a new change, make it possible to store multiple documents against an `EquipmentLocation` so that equipment can have both pdfs and xls at the same time. 
    Refactor the model `EquipmentManual` to be called `EquipmentDocument` and the `EquipmentLocation`.`manual` field to be called `EquipmentLocation`.`documents`.
    
Requirements: 
* Ensure that the data which existed as `EquipmentManual`.`manual` is migrated across into `EquipmentLocation`.`documents` (preserve the existing data).
* Update the existing api's to reflect the new changes by refactoring `manual_id` on the payload, to `documents` as an array.
* Implement a limitation of 5 documents per `EquipmentLocation`.

Sample Payload:
```json
{
  "id": 1,
  "type_id": 1,
  "name": "Some Sample Equipment",
  "site_id": 1,
  "line_id": null,
  "location_path": "some_sample_equipment",
  "part_number": null,
  "documents": [
    1,
    2,
    3
  ],
  "children": null
}
```

4.) _An api user wants to find all equipment as well as any equipment under that equipment 1) by searching using the equipment name 2) by searching by the equipment type_. 

    Create a way to filter data by using API queries on READing `EquipmentLocation` data. 
    An API user needs to query against `EquipmentLocation`.`name` to find all equipment containing a query term. 

Requirements:
* An API should be able to be filtered down by equipment with the names that contain the term(as-well-as a tree of the children) returning the `EquipmentLocation` nodes which were found.
* An API should be  able to be filtered down by the type_id returning the nodes which were found.
* the search on name should ideally be sort of like... `%LIKE%`
* the search on type should be exact match. 

_Thanks for participating!_
