// tutorial4.js
var Series = React.createClass({
  render: function() { 
    return (
        <div className="pullLine">
            <span><a href="/issues/{this.props.series}">{this.props.seriesName}</a></span>
            <span className="pull-right">
                <a href={"/pull/delete/"+this.props.id}>Remove</a> |
                <a onclick="javascript:transfer_unread_primaries('{this.props.id}', 'True');">Transfer Unread Primaries</a>
            </span>
        </div>
    );
  }
});

// tutorial2.js
var PullsList = React.createClass({
  render: function() {
    var pullList = this.props.data.map(function(pulls) {
      return (
        <Series seriesName={pulls.series__name} series={pulls.series} id={pulls.id} />
      );
    });
    return (
      <div className="commentList">
        {pullList}
      </div>
    );
  }
});

var PullsWrapper = React.createClass({
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
      // setInterval(this.loadCommentsFromServer, this.props.pollInterval);
    },
    render: function() {
      return (
        <div className="pullLists">
          <PullsList data={this.state.data} />
        </div>
      );
    }
});