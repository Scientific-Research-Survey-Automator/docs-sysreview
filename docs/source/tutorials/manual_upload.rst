Manually uploading results
^^^^^^^^^^^^^^^^^^^^^^^^^^
The searched results that we saw earlier are collected from respective research databases through their API.
Sometimes certain results may appear elsewhere like their respective portals but not through their APIs.

In order to address this limitation, we have an option to manually patch search results to a query along with API fetched results.
This helps in managing our survey results.

Search results are classified based on their source, i.e. the API datasource however if uploaded manually, it would be classified as Manual.

So let us continue with the previous example, based on the query and research we will upload results manually
and associate with our query.

.. note::

   You cannot add results manually if you have saved your query, so ensure your query is still in draft mode and not saved.


1. Within your query card add datasource :guilabel:`MANUAL` and then click on :guilabel:`UPLOAD` button

.. image:: /images/tutorials/queries/manual/query_card_manual.png

2. You will see the Manual upload menu has popped up.
You can upload a CSV file containing search results and select the template type for which the header configuration is displayed below.

.. image:: /images/tutorials/queries/manual/manual_upload_menu.png

3. By clicking upon the :guilabel:`Preview` button, it will download the header configuration in a json file.
You can use this file to edit and make your own config. If you're making your own config
then change the template type to :guilabel:`CUSTOM` and upload your configuration first.

.. image:: /images/tutorials/queries/manual/manual_upload_custom_template.png

4. Now upload your prepared search results in a CSV formatted file.
For this we can run a query on `PubMed <https://pubmed.ncbi.nlm.nih.gov/?term=%27machine+learning%27+and+%27healthcare%27+and+%27blockchain%27&schema=alltitle>`_
and export this result to CSV file and upload this file by clicking on the blue :guilabel:`Upload` button

.. image:: /images/tutorials/queries/manual/manual_upload_pubmed.png

5. Now you can see upon uploading the manual card has updated with the total number of result it has uploaded and then you can click on the card to see this detailed view.

.. image:: /images/tutorials/queries/manual/manual_pubmed_results.png

6. Now the total results including the API fetched results and manually uploaded results can be seen by clicking on the :guilabel:`Show All` button.
