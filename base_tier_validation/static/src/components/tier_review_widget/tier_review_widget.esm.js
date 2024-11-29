/** @odoo-module **/

import {registry} from "@web/core/registry";

import {useService} from "@web/core/utils/hooks";

const {Component} = owl;

export class ReviewsTable extends Component {
    setup() {
        this.collapse = false;
        this.orm = useService("orm");
        this.reviews = [];
    }
    _getReviewData() {
        const records = this.env.model.root.data.review_ids.records;
        const reviews = [];
        for (var i = 0; i < records.length; i++) {
            reviews.push(records[i].data);
        }
        return reviews;
    }
    onToggleCollapse(ev) {
        console.log(ev.target,'+++++++++') 
        // var $panelHeading = $(ev.target).closest(".panel-heading"); //$(ev.currentTarget)
        if (this.collapse) {
            document.querySelector('#collapse1').style.display = 'none';
            //     $panelHeading.next("div#collapse1").hide();
        } else {
            document.querySelector('#collapse1').style.display = 'block';
            //     $panelHeading.next("div#collapse1").show();
        }
        this.collapse = !this.collapse;
    }
}

ReviewsTable.template = "base_tier_validation.Collapse";

export const reviewsTableComponent = {
    component: ReviewsTable,
};

registry.category("fields").add("form.tier_validation", reviewsTableComponent);
