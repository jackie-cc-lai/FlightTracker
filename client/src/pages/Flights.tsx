import React from 'react';

interface Props {
    prop1: any;
}
function Flights({prop1}: Props) {
    return <div>{prop1}</div>
}

export default Flights;