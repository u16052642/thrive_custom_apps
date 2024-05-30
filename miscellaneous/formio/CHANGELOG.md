# Changelog

## 17.0.2.0.1

- Fix migration scipts to support big jumps/leaps without crashing due to non-existent fields.
- Form Builder: Add badge "Locked Disabled".

## 17.0.2.0.0

Rename and migrate Form Builder field `public_uuid` to `current_uuid`.\
The `current_uuid` is a more meaningful name.

## 17.0.1.8

In Form Builder views (list, form, search) add:
- Field Public UUID (`public_uuid`)
- Public Current URL (`public_current_url`)

This is in addition to version 17.0.1.5.

## 17.0.1.7

Migrate the Form Builder (`formio.builder`) field `submission_url_add_query_params_from` to endpoint specific fields:
- `portal_submission_url_add_query_params_from`
- `portal_submission_url_add_query_params_from`
- `backend_submission_url_add_query_params_from`

This makes it possible to distinguish the setting per endpoint.

## 17.0.1.6

Minor form builder view migration fix (column_invisible).

## 17.0.1.5

### Allow (support) versioning for publicly published forms (form builders)

Add endpoint `/formio/public/form/new/current/<string:builder_public_uuid>` that allows to update the form builders (versioning) and keep them published when the state is "Current".\
This required to add the `formio.builder` model field `public_uuid`, that is identical to all `formio.builder` records with the same name.

## 17.0.1.4

In the Form Builder, show a "Locked" badge in case it is locked.

## 17.0.1.3

Add new group "Forms: Allow updating form submission data".\
Users in this group are allowed to edit and update the (raw, JSON) submission data in the `formio.form` form view.

## 17.0.1.2

- Fix formioScrollIntoView event handler.
- Default value for form builder fields: `portal_scroll_into_view`, `public_scroll_into_view`

## 17.0.1.1

Improve the formio.js library registration (downloader, importer) with a new setting to allow only registered versions.\
This adds a new system parameter `ir.config_parameter` which currently defaults to 'v4' and can be modified in the configuration window.\
The allowed setting is a comma separated string (list) of formio.js versions to register. Examples:
- v4,v5
- v4.17,v4.18

## 17.0.1.0

Initial release.
