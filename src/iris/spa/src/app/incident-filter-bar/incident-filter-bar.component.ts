import { Component, inject } from '@angular/core';
import { NgbCalendar, NgbDatepickerModule, NgbDateStruct } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule } from '@angular/forms';
  
@Component({
  selector: 'app-incident-filter-bar',
  imports: [NgbDatepickerModule, FormsModule],
  templateUrl: './incident-filter-bar.component.html',
  styleUrl: './incident-filter-bar.component.scss'
})
export class IncidentFilterBarComponent {
  today = inject(NgbCalendar).getToday();
  
  model!: NgbDateStruct;
}
