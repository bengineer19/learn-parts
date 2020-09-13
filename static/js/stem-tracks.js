var playlist = WaveformPlaylist.init({
  samplesPerPixel: 1000,
  waveHeight: 100,
  container: document.getElementById("playlist"),
  timescale: true,
  state: "cursor",
  colors: {
    waveOutlineColor: "#E0EFF1",
  },
  controls: {
    show: true, //whether or not to include the track controls
    width: 200, //width of controls in pixels
  },
  zoomLevels: [500, 1000, 3000, 5000],
});

playlist
  .load([
    {
      src: "/audio/1kdn-kwUQB-kPujpX6S2huBAwEyiv9A09",
      name: "EP",
      // gain: 0.75,
    },
    {
      src: "/audio/1uY67Q1K_kq5ZOwZ9sQ394gEB8dOz6wwE",
      name: "Drums",
    },
    {
      src: "/audio/1rPdE0seMLnFqU7-m3LKEE0pVgcHsIxxJ",
      name: "Vox",
    },
  ])
  .then(function () {
    //can do stuff with the playlist.
  });
