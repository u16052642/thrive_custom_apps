.. _api-queue:

#####
Queue
#####

Models
******

.. automodule:: thrive.addons.queue_job.models.base
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: thrive.addons.queue_job.models.queue_job

   .. autoclass:: QueueJob

     .. autoattribute:: _name
     .. autoattribute:: _inherit

***
Job
***

.. automodule:: thrive.addons.queue_job.job

   Decorators
   ==========

   .. autofunction:: job
   .. autofunction:: related_action

   Internals
   =========

   .. autoclass:: DelayableRecordset
      :members:
      :undoc-members:
      :show-inheritance:

   .. autoclass:: Job
      :members:
      :undoc-members:
      :show-inheritance:
