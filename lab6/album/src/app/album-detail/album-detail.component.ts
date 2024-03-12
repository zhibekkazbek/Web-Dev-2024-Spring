import { Component } from '@angular/core';
import {ActivatedRoute, RouterModule} from "@angular/router";
import {CommonModule} from "@angular/common";
import {FormsModule} from "@angular/forms";
import {AlbumsService} from "../albums.service";

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [RouterModule, CommonModule, FormsModule],
  templateUrl: './album-detail.component.html',
  styleUrl: './album-detail.component.css'
})
export class AlbumDetailComponent {
  albumId: number = 0;
  album: any;
  editedTitle: string = "";

  constructor(private route: ActivatedRoute, private albumsService: AlbumsService) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.albumId = +params['id'];
      this.albumsService.getAlbumById(this.albumId).subscribe(album => {
        this.album = album;
        this.editedTitle = album.title;
      });
    });
  }

  saveChanges(){
    this.album.title = this.editedTitle;
    this.albumsService.updateAlbumTitle(this.albumId, this.editedTitle).subscribe(() => {
      console.log('Album title updated successfully!');
    });
  }
}
