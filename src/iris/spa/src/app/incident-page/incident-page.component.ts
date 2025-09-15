import { Component } from '@angular/core';
import { NgbNavModule } from '@ng-bootstrap/ng-bootstrap';
import { IncidentFilterBarComponent } from '../incident-filter-bar/incident-filter-bar.component';
import { IncidentResultsTableComponent } from "../incident-results-table/incident-results-table.component";

@Component({
  selector: 'app-incident-page',
  imports: [NgbNavModule, IncidentFilterBarComponent, IncidentResultsTableComponent],
  templateUrl: './incident-page.component.html',
  styleUrl: './incident-page.component.scss'
})
export class IncidentPageComponent {
  dismissable = false;
}
