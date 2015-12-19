var PhotoThumbnail = React.createClass({
  render: function() {
    var img_file = "/static/images/"+this.props.file;
    var img_url = "/comics/"+this.props.id;
    return(
        <a href={img_url}><img src={img_file} width="160px" /></a>
    );
  },
});

var PhotoStripList = React.createClass({
  render: function() {
    var photoList = this.props.data.map(function(photo) {
      return (
        <PhotoThumbnail key={photo.id}
                        width={160}
                        id={photo.id}
                        file={photo.thumbnail}
                        name={photo.comic_name} />
      );
    });
    return (
      <div className="thumbs">
        {photoList}
      </div>
    );
  }
});

var PhotoStripWrapper = React.createClass({
    loadPullsFromServer: function() {
      $.ajax({
        url: this.props.url,
        dataType: 'json',
        cache: false,
        success: function(data) {
          this.setState({data: data});
        }.bind(this),
        error: function(xhr, status, err) {
          console.error(this.props.url, status, err.toString());
        }.bind(this)
      });
    },
    getInitialState: function() {
      return {data: []};
    },
    componentDidMount: function() {
      this.loadPullsFromServer();
    },
    render: function() {
      return (
        <div className="thumbsLists">
          <PhotoStripList data={this.state.data} />
        </div>
      );
    }
});