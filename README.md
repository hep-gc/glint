glint
=====

Glint is a cloud image distribution service built using the django framework. Glint currently supports Openstack clouds. Glint extends Horizon to add image distribution functionality to Horizon's Image Management interface. 

Glint uses Openstack's Glance Image Management API to manage images on multiple Openstack clouds in a consolidated way. Glint offers two main services: the Site Management and User Credential Service, and the Image Distribution Service.

The Site Management and User Credential Service allows users to identify other Openstack sites. It also allows users to store their credentials for sites, which Glint uses for authorization to modify that site's Glance repository.

The Image Distribution Service uses Glance to identify all images across all sites, and creates a simple table for the user to easily select which images they want to have on selected sites.

Glint uses Glance to transfer images from source sites to destination sites using the Glance API.

To setup and use glint, please clone the the glint-service setup scripts at https://github.com/rd37/glint-service , and follow the README 

