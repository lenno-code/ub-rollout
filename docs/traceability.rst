Traceability
============

This section provides various views of requirements traceability.

Requirements Overview
---------------------

All requirements and their current status:

.. needtable::
   :filter: type == 'req'
   :columns: id;title;status;priority
   :style: table
   :sort: id

Full Traceability Flow
----------------------

This diagram shows how requirements, specifications, and tests
connect:

.. needflow::
   :filter: type in ['req', 'spec', 'test']
   :engine: plantuml
   :show_link_names:
   :show_legend:

Specifications Matrix
---------------------

Which requirements are covered by specifications:

.. needtable::
   :filter: type == 'spec'
   :columns: id;title;status;implements
   :style: table

Test Coverage
-------------

Which specifications have test cases:

.. needtable::
   :filter: type == 'test'
   :columns: id;title;status;tests
   :style: table

Open Items
----------

All items that are not yet done:

.. needtable::
   :filter: status == 'open'
   :columns: id;type;title;status
   :style: table
   :sort: type