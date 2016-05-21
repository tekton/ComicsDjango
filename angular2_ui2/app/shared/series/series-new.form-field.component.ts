import { Component, Input } from '@angular/core';
import { ControlGroup }     from '@angular/common';
import { FieldBase } from '../base.field';
@Component({
    selector: 'df-field',
    templateUrl: '/static/app/shared/series/series-new.form-field.component.html',
})
export class DynamicFieldComponent {
    @Input() question: FieldBase<any>;
    @Input() form: ControlGroup;
    get isValid() { return this.form.controls[this.question.key].valid; }
}