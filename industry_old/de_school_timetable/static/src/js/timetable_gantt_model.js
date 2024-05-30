thrive.define('de_school_timetable.TimetableGanttModel', function (require) {
"use strict";

var GanttModel = require('de_school_timetable.GanttModel');
var _t = require('web.core')._t;

var TimetableGanttModel = GanttModel.extend({
    /**
     * @private
     * @override
     * @returns {Object[]}
     */
    _generateRows: function (params) {
        // provide group for unassigned timetable
        if(params.groupedBy.length) {
            var groupedByField = params.groupedBy[0];
            if (groupedByField === 'teacher_id') {
                var empty_exists = _.some(params.groups, function(group) {return !group[groupedByField];});
                if (!empty_exists) {
                    var values = this._parsePath(params.parentPath);
                    var new_group = _.clone(values);
                    new_group = _.extend(new_group, {
                        id: _.uniqueId('group'),
                        fake: true,
                        __count: 0,
                        __domain: this._getDomain(), // TODO: add the domain part with the values
                        user_id: false,
                    });
                    params.groups.push(new_group);
                    this.ganttData.groups.push(new_group);
                }
            }
        }

        var rows = this._super(params);

        // rename undefined assigned to
        _.each(rows, function(row){
            if(row.groupedByField === 'teacher_id' && !row.resId){
                row.name = _t('Unassigned Tasks');
            }
        });
        // is the data grouped by?
        if(params.groupedBy && params.groupedBy.length){
            // in the last row is the grouped by field is null
            if(rows && rows.length && rows[rows.length - 1] && !rows[rows.length - 1].resId){
                // then make it the first one
                rows.unshift(rows.pop());
            }
        }
        return rows;
    },
    /**
     * Parse the path of a group, according to the groupedBy fields, in order to extract
     * default value of a group.
     *
     * @private
     */
    _parsePath: function(path) {
        var values = {};
        if (path) {
            var pathParts = path.split('\n');
            var state = this.get();
            var groupby = state.groupedBy;
            _.each(groupby, function(fname, index) {
                var val = pathParts[index];
                if (val) {
                    val = JSON.parse(val);
                    if (state.fields[fname].type == 'many2one') {
                        values[fname] = val[0];
                    } else {
                        values[fname] = val;
                    }
                }
            });
        }
        return values;
    },
});

return TimetableGanttModel;
});