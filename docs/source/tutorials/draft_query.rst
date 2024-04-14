Designing queries
~~~~~~~~~~~~~~~~~

Drafting query
^^^^^^^^^^^^^^

Now that you've successfully created your account and configured your project and its settings,
it is time to design and execute your queries.
In order to create a query click on the :guilabel:`+` icon button on the query panel.
This will create a query draft and you can see the card below the query panel

.. image:: /images/tutorials/queries/draft/query_draft_card.png

Click on the card to design the query, this will open the query dialog. Provide the following details:

* Name: meaningful name associated with the nature of this query
* Query: actual query containing keywords and boolean operators such AND, OR
* Date Range: you can provide a month range `(optional)` parameter to search results between this range, ensure you enable the checkbox to include date range in search

To design queries there are two ways:

1. As an interdisciplinary researcher, if you're well-versed with the syntax of designing queries to search across these
scientific research databases, you can manually enter the query text
2. We have a tool called querybuilder to build queries that can help in designing meaningful queries that have higher
complexity such as nested logic, multiple kinds of operators which will also help in visualizing

Using querybuilder
^^^^^^^^^^^^^^^^^^
In order to use querybuilder click on the yellow :guilabel:`🔧` icon button in the query field, this will open a popup
showing the querybuilder dialog box. Now you can design query rules or create groups of sub-queries and continue building your intended logic.

Let us consider an example, I would like to find research papers relating to machine learning in healthcare using blockchain.
We need to identify the keywords for this query and divide them in groups:

* Group 1: could contain 'machine learning' and 'healthcare'
* Group 2: could contain just 'blockchain'

To accommodate all the permutations of the keywords in each group and also ensure inclusivity of both groups together
we would need to use both `AND` and `OR` operator

This can be easily design in query builder, to create group 1 simply click on the grey :guilabel:`+Group` button
and to add keywords inside or outside group click on the blue :guilabel:`+Rule` button

.. image:: /images/tutorials/queries/draft/querybuilder.png

Click on the blue :guilabel:`Use Query` button at the bottom right of the dialog box
after you're done using the querybuilder to generate query text.
