
function University() {
    this.name = 'Example University';
    this.address = '11235 Some Random Road';
    this.termsPerYear = 3;
}

function Meeting() {
    this.startTime = new Date();
    this.endTime = new Date();

    this.startTime.setHours(8);
    this.startTime.setMinutes(0);
    this.endTime.setHours(9);
    this.endTime.setMinutes(30);

    this.room = '';
}

function Section() {
    this.name = 'S??';
    this.meetings = [ new Meeting() ];
}

function Course() {
    this.code = 'TESTING';
    this.name = 'Example Course';
    this.description = 'Lalala this is an example course blah blah blah';
    this.section = new Section();
    this.university = null;
}

function Schedule() {
    
}

