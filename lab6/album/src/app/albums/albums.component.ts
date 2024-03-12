import {Component, OnInit} from '@angular/core';
import {RouterModule, ActivatedRoute } from "@angular/router";
import {CommonModule} from "@angular/common";
import {AlbumsService} from "../albums.service";

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [RouterModule, CommonModule],
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent implements OnInit {
  albums: any[] = [];

  constructor(private albumsService: AlbumsService) { }

  ngOnInit() {
    this.albumsService.getAlbums().subscribe(albums => {
      this.albums = albums;
    });
  }

  deleteAlbum(albumId: number) {
    this.albumsService.deleteAlbum(albumId).subscribe(() => {
      // Remove the deleted album from the list
      this.albums = this.albums.filter(album => album.id !== albumId);
    });
  }
}
