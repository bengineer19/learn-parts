var playlist = WaveformPlaylist.init({
  samplesPerPixel: 8000,
  waveHeight: 100,
  container: document.getElementById("playlist"),
  timescale: true,
  state: "cursor",
  colors: {
    waveOutlineColor: "white",
  },
  controls: {
    show: true, //whether or not to include the track controls
    width: 200, //width of controls in pixels
  },
  zoomLevels: [500, 1000, 2000, 4000, 6000, 8000],
});

playlist.load(song.tracks).then(function () {
  document.getElementById("loader").style.display = "none";
});
