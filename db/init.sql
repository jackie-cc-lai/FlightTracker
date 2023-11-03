CREATE TABLE flight_info (
	fa_flight_id text PRIMARY KEY,
	origin varchar(4) references airports(code_iata),
	destination varchar(4) references airports(code_iata),
	codeshares_iata text[],
	codeshares text [],
	operator text NOT NULL,
	ident_iata text NOT NULL,
	ident_icao text NOT NULL,
	departure_delay int,
	arraival_delay int,
	filed_ete int NOT NULL,
	scheduled_out TIMESTAMPTZ NOT NULL,
	scheduled_off TIMESTAMPTZ NOT NULL,
	scheduled_on TIMESTAMPTZ NOT NULL,
	scheduled_in TIMESTAMPTZ NOT NULL,
	estimated_off TIMESTAMPTZ,
	estimated_out TIMESTAMPTZ,
	estimated_in TIMESTAMPTZ,
	estimated_on TIMESTAMPTZ,
	actual_in TIMESTAMPTZ,
	actual_on TIMESTAMPTZ,
	actual_off TIMESTAMPTZ,
	actual_out TIMESTAMPTZ,
	aircraft_type text NOT NULL,
	route_distance int,
	cancelled bool NOT NULL,
	progress_percent int,
	status text NOT NULL,
	flight_image text
);

CREATE TABLE users (
    id uuid PRIMARY KEY,
    email text NOT NULL,
    name text,
    created_on timestamp,
    password char(64)
);

CREATE TABLE user_flights (
    id uuid PRIMARY KEY,
    user_id uuid references users(id),
    flight_id text references flight_info(fa_flight_id),
    created_on timestamp NOT NULL
);