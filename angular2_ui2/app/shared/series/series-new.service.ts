import { Injectable }   from '@angular/core';
import { ControlGroup, FormBuilder, Validators } from '@angular/common';
import { FieldBase } from '../base.field';
import {TextboxField} from "../textbox.field"

@Injectable()
export class SeriesNewService {
    constructor(private fb: FormBuilder) { }

    toControlGroup(questions: FieldBase<any>[]) {
        let group = {};

        questions.forEach(question => {
            group[question.key] = question.required ? [question.value || '', Validators.required] : [question.value || ''];
        });
        return this.fb.group(group);
    }

    getFields(){
        let questions: FieldBase<any>[] = [
            new TextboxField({
                key: 'start',
                label: 'First Numbered Issue',
                value: '1',
                required: true,
                order: 1
            }),
            new TextboxField({
                key: 'end',
                label: 'Last Numbered Issue',
                value: '1',
                order: 2
            }),
            new TextboxField({
                key: 'name',
                label: 'Series Name',
                value: '',
                required: true,
                order: 5
            })
        ];
        return questions.sort((a, b) => a.order - b.order);
    }
}