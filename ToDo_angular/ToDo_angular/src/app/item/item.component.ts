import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Item } from "../item";

@Component({
  selector: 'app-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './item.component.html',
  styleUrl: './item.component.css'
})
export class ItemComponent {
  // When you use a property in the template, must declare in the class
  editable = false;

  // Communication between two components
  /* @Input() = doorway for data to come into the component
   *            - use to specify that the value can come from outside the component
   * @Output()= doorway for data to go out of a component
   *            - must be of type EventEmitter()
   *            - to specify that the value of a prop can leave the component and
   *              another component can receive it
   *            - so that a component can raise an event when there's data ready
   *              to share with another component
   * Note: the ! in the class's property declaration = definite assignment assertion
   *            - tells TS the item field is always initialized and not undefined even
   *              if TS cannot tell from the constructors definition
   *            - if not included and have strict TS compilation settings, app will
   *              fail to compile
  */
  @Input() item!: Item;
  @Output() remove = new EventEmitter<Item>();

  saveItem(description: string) {
    if (!description) return;

    this.editable = false;
    this.item.description = description;
  }
}

