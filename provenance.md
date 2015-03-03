# S A M P L E

## Components and Licensing

The CANARIE reference service is written in Python and contains the following components:
  * Version 2.7 of the Python runtime environment and standard libraries. Licence: http://docs.python.org/2/license.html
  * Version 1.4.3 of the Django web framework. Licence: https://github.com/django/django/blob/master/LICENSE
  * Custom Software developed at CANARIE. Licence: https://github.com/canarie/research_software/blob/master/reference/licence.md  

### Versioning

The Reference Service software is identified by  a version identifier in the x.y format, where x is a positive integer and and y is a positive integer or zero. An increase in the major number ("x") indicates as significant change that would make this version incompatible with previous versions. Examples of such a change would include changes to the database schema or support for a new version of the CANARIE protocol used to communicate with this service. An increase in the minor number ("y") indicates minor changes such as bug fixes and performance improvements. The initial release is 1.0.


### Release and Deployment Criteria

Both the CANARIE Lead Software Architect and Test Engineer must approve the release of the Reference Service software. Once approved, the service is deployed on our virtual machines at abtest.canarie.ca and qctest.canarie.ca and the corresponding source code and documentation are pushed from our internal revision control system to GitHub at https://github.com/canarie/research_software/tree/master/reference. This code and documentation are tagged with the version number of the release, as described above.

# S A M P L E
