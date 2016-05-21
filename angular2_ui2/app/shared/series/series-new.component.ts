import { Component }       from '@angular/core'
import { SeriesNewForm }     from './series-new.form';
import { SeriesNewService } from './series-new.service';
@Component({
  selector: 'series-new',
  template: `
    <div>
      <h2>New Series</h2>
      <series-new [questions]="questions"></series-new>
    </div>
  `,
  directives: [SeriesNewForm],
  providers: [SeriesNewService]
})
export class SeriesNewComponent {
  questions:any[]
  constructor(service: SeriesNewService) {
    this.questions = service.getFields();
  }
}