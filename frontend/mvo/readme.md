# Model View Octopus


## Model

Models provide an interface for mutating your application data.
  - If the application persists data, either over HTTP or Local Storage, the Model should provide an interface to manipulate this data.
  - Models **do not** render content or interact with the DOM.


## View

A View renders your application UI. In web the View is responsible for manipulating the DOM based on the current state of the Model.
  - References to DOM elements is exclusive to the View.
  - Since only the view knows when a DOM element is created or destroyed, it is the responsibility of the View to bind and unbind from events. The View generally passes these events to the Octopus where business logic or Model manipulation occurs.
  - The View renders elements based on the current state of the Model as passed by the Octopus, but never changes or depends on the Model directly.


## Octopus

Also known as **Controller**, **ViewModel**, **whatever**.

Views do not directly interact with Models, or vice versa. It is the responsibilty of the octopus to facilitate interactions between the View and Model.
