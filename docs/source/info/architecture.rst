************
Architecture
************

Overview
========
.. image:: /images/information/architecture.png

The architecture of SysReview is designed to provide a robust and scalable framework for conducting systematic reviews
efficiently across diverse research domains. It encompasses various components, modules, and layers that work
synergistically to facilitate seamless data retrieval, processing, analysis, and reporting.

Aspects
=======

Frontend Interface
---------------------
.. figure:: /images/information/architecture_frontend.png
   :alt: frontend architecture
   :width: 150
   :height: 150
   :scale: 75 %
   :align: right

* The frontend interface serves as the user-facing component of SysReview, providing researchers with intuitive tools and interfaces to interact with the system.
* Built using modern web technologies such as HTML, CSS, and React(e.g., JavaScript frameworks ), the frontend interface offers a responsive and user-friendly experience across different devices and platforms.


Backend Services
-------------------
.. figure:: /images/information/architecture_backend.png
   :alt: backend architecture
   :width: 150
   :height: 150
   :scale: 75 %
   :align: left

* The backend services of SysReview encompass the core logic and functionality of the system, handling tasks such as user/account session management, configuring projects, query processing, data retrieval, categorising results, and curation tracking.
* Implemented using server-side technologies such as Java and Spring Boot, the backend services provide robust APIs for communication between the frontend interface and the underlying data processing modules.
* These services orchestrate the systematic review process, co-ordinating the execution of various tasks and workflows to ensure seamless integration and data flow.
* Integrated with swagger to generate API documentation that can be accessed from `here <https://sysrev.cs.binghamton.edu/sysreview/swagger-ui/>`_.

Data Processing Modules
--------------------------
.. image:: /images/information/datasources.png

* At the heart of SysReview are the data processing modules responsible for retrieving, standardizing, and analyzing research articles from diverse sources.
* These modules leverage APIs and web scraping techniques to extract data from research hosting databases such as Web of Science, PubMed, IEEE, Scopus, and others.
* The data processing module is generic, with ability to accommodate multiple datasources.

Database and Storage
-----------------------
.. figure:: /images/information/architecture_db.png
   :alt: database architecture
   :width: 150
   :height: 150
   :scale: 75 %
   :align: right

* SysReview relies on a robust database and storage infrastructure to store and manage project configuration, research articles, query metadata, user preferences, and other relevant data.
* Postgres database is leveraged to maintain the relational data across different components and provide ability to store and retrieve data as traffic scales.
* Research documents retrieved from different sources are standardised on this platform however can be unstructured/semi-structured with nested complexities. Postgres offers ability to store JSON objects without compromising on our relational schema for other entities.

Security and Authentication
------------------------------
.. figure:: /images/information/architecture_auth.png
   :alt: auth architecture
   :width: 150
   :height: 150
   :scale: 75 %
   :align: left

* Security measures such as encryption, authentication, and access control mechanisms are integrated into the architecture of SysReview to safeguard sensitive data and user information.
* User authentication and authorization mechanisms are employed using JWT (JSON Web Tokens) to ensure secure access to the system and protect against unauthorized access.

Summary
=======
In summary, the architecture of SysReview provides a flexible, scalable, and secure framework for conducting systematic reviews effectively and efficiently. By leveraging advanced technologies and methodologies, SysReview empowers researchers to navigate the complexities of research literature with confidence, facilitating the synthesis of evidence and the advancement of knowledge across diverse research domains.