import { FieldBase } from './base.field';

export class TextboxField extends FieldBase<string>{
    controlType = 'textbox';
    type: string;

    constructor(options: {} = {}) {
        super(options);
        this.type = options['type'] || '';
    }
}