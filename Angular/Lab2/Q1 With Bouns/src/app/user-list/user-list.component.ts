import { CommonModule} from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './user-list.component.html',
  styleUrl: './user-list.component.css'
})
export class UserListComponent {
  users: any[] = [];
  filteredUsers: any[] = [];
  searchEmail: string = '';
  showResetButton: boolean = false;

  constructor() {
    this.loadUsers();
  }


  loadUsers() {
    fetch('assets/users.json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to load users.json');
        }
        return response.json();
      })
      .then(data => {
        this.users = data;
        this.filteredUsers = data;
      })
      .catch(error => {
        console.error('Error loading users:', error);
      });
  }

  resetSearch() {
    this.searchEmail = '';
    this.filteredUsers = this.users;
    this.showResetButton = false;
  }


  applyFilter() {
    this.filteredUsers = this.users.filter((user) =>
      user.email.toLowerCase().includes(this.searchEmail.toLowerCase())
    );
    this.showResetButton = true;
  }
}
