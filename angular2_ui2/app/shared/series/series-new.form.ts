import { Component, Input, OnInit }  from '@angular/core';
import { ControlGroup }              from '@angular/common';
import { FieldBase } from '../base.field';
import { SeriesNewService }       from './series-new.service';
import { DynamicFieldComponent } from './series-new.form-field.component';

@Component({
  selector: 'series-new',
  templateUrl: '/static/app/shared/series/series-new.html',
  directives: [DynamicFieldComponent],
  providers: [SeriesNewService]
})
export class SeriesNewForm {
  @Input() questions: FieldBase<any>[] = [];
  form: ControlGroup;
  payLoad = '';
  constructor(private qcs: SeriesNewService) { }
  ngOnInit() {
    this.form = this.qcs.toControlGroup(this.questions);
  }
  onSubmit() {
    this.payLoad = JSON.stringify(this.form.value);
  }
}