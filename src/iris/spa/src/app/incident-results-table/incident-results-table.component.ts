import { Component } from '@angular/core';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-incident-results-table',
  imports: [NgFor],
  templateUrl: './incident-results-table.component.html',
  styleUrl: './incident-results-table.component.scss'
})
export class IncidentResultsTableComponent {
  incidents = [
    { id: 1, title: 'Incident 1', status: 'Open' },
    { id: 2, title: 'Incident 2', status: 'In Progress' },
    { id: 3, title: 'Incident 3', status: 'Closed' }
  ];
}
