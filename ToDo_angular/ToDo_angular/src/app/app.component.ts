import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'
import { Item } from "./item";
import { ItemComponent } from "./item/item.component";

@Component({
  standalone: true,
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css', // styleUrls: ['./pathtostyles.css']
//  styles: ['h1 { color: red; }'] EXAMPLE
  imports: [CommonModule],
})
export class AppComponent {
  componentTitle = 'My To Do List';

  // Filter property is of type UNION " x | y | z"
  filter: "all" | "active" | "done" = "all";

  // Sample items
  allItems = [
    {description: "eat", done: true},
    {description: "sleep", done: false},
    {description: "play", done: false},
    {description: "laugh", done: false},
  ];

  // Add items to the todo list
  addItem(description: string) {
    if (!description) return;

    // Array method: unshift = add a new item to the beginning of the array and
    //  top of the list
    //  push() = add item to the end of the array and bottom of the list
    this.allItems.unshift({
      description,
      done: false
    })
  };

 // Remove items from the todo list
 /* splice() = changes contents of an array by removing or replacing existing
               elements and/or adding new elements in place */
  remove(item: Item){
    this.allItems.splice(this.allItems.indexOf(item), 1);
  }

  // Retrieves the items from the allItems array if the filter === all
  // Otherwise, returns the done or pending items depending on how user filters view
  // Establishes name of array as items
  get items() {
    if (this.filter === "all") {
      return this.allItems;
    }
    return this.allItems.filter((item) =>
    this.filter === "done" ? item.done : !item.done
    );
  }
}
