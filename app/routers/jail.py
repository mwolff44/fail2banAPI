# Copyright 2019 (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

@router.get("/jail/{jail}", response_model=)

@router.post("/jail/{jail}/ban", response_model=)

@router.post("/jail/{jail}/unban", response_model=)

@router.post("/jail/{jail}/failregex", response_model=)

@router.delete("/jail/{jail}/failregex", response_model=)
