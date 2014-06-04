glint
=====

Glint is a cloud image distribution service built using the the django framework. Glint currently supports openstack clouds. Glint extends horizon to add image distribution specific functionality to Horizon's Image management interface. 

Glint uses openstack's Glance Image management api to aggregate distributed openstack clouds. Glint offers two main services. The site management and user credential service and the image distribution service.

The site management and user credential service allows users to identify other openstack sites. It also allows users to store their credentialis for there sites that Glint uses to login and modify that sites glance repository.

The image distribution service uses glance to identify all images accross all sites and creats a simple table for the user to easily select which images they want on selected sites.

Glint uses glance to transfer images from source sites to destination sites using the Glance API.

