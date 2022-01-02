export function addTableComponent(app) {

    app.component("vue-table-row", {
        template: "#vue-table-row-template",
        props: {
            item: Array
        }
    });

    app.component("vue-table", {
        template: "#vue-table-template",
        props: {
            headerColumns: Array,
            items: Array,
            // loop variable
            item: Array
        },
        computed: {
            tableRowComponent: function() {
                return 'vue-table-row';
            },
            calculatedHeaderColumns: function() {
                return this.headerColumns;
            }
        }
    });
}

